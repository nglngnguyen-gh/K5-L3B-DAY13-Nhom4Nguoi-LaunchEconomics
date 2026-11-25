r"""Xuất số liệu slide từ code lab, không chép lại kết quả bằng tay.

Chạy bằng môi trường lab: .venv\Scripts\python.exe presentation\cp1_cp2\collect_data.py
"""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'src'))
import pandas as pd
import lab13


def collect():
    runs = pd.read_csv(ROOT / 'src/logix_runs.csv')
    reqs = pd.read_csv(ROOT / 'src/logix_requests.csv', keep_default_na=False)
    lab13.kiem_tra_dap_an_biet_truoc()
    core = lab13.mo_hinh(runs, reqs)
    scope_reqs = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    scope = lab13.mo_hinh(runs, scope_reqs)
    types = []
    joined = runs.merge(reqs[['request_id', 'loai']], on='request_id', validate='many_to_one')
    for kind in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        group = reqs[reqs.loai == kind]
        result = lab13.mo_hinh(runs, group)
        attempts = joined[joined.loai == kind].groupby('attempt').status.apply(lambda x: x.eq('ok').mean())
        types.append(dict(kind=kind, requests=len(group), success_rate=result['thanh_cong'] / len(group),
                          mean_attempts=float(group.so_lan_chay.mean()), cps=result['cps'],
                          ratio=result['cps'] / lab13.BASELINE, attempt_ok=attempts.tolist()))
    fixed = []
    for volume in [45000, 22500]:
        successes = volume * scope['thanh_cong'] / len(reqs)
        per_success = 40000000 / successes
        fixed.append(dict(volume=volume, successes=successes, fixed=per_success,
                          cps=scope['cps'] + per_success))
    sensitivities = [dict(name=name, cps=value['cps'], change=100 * (value['cps'] / core['cps'] - 1))
                     for name, value in lab13.do_nhay(runs, reqs).items()]
    paired = lab13.mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    retry = []
    for limit in [1, 2, 3]:
        value = lab13.mo_hinh(runs, reqs, max_lan_chay=limit)
        failures = len(reqs) - value['thanh_cong']
        retry.append(dict(limit=limit, total=value['tong'], failures=failures,
                          system=value['tong'] + failures * lab13.BASELINE, cps=value['cps']))
    mean_rework = float(reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean())
    b4 = [dict(minutes=minutes, **lab13.xem_lai_toan_bo(runs, reqs, phut_lam_lai=minutes))
          for minutes in [9, mean_rework]]
    sha = subprocess.check_output(['git', '-c', f'safe.directory={ROOT.as_posix()}', '-C', str(ROOT),
                                   'rev-parse', '--short', 'HEAD'], text=True).strip()
    return dict(source_commit=sha, requests=len(reqs), runs=len(runs),
                baseline=lab13.BASELINE, core=core, types=types, scope=scope,
                scope_requests=len(scope_reqs), fixed=fixed, sensitivity=sensitivities,
                paired=paired, paired_change=100 * (paired['cps'] / core['cps'] - 1),
                retry=retry, b4=b4, system_per_request=retry[-1]['system'] / len(reqs),
                human_share=100 * (core['xem_lai'] + core['lam_lai']) / core['tong'])


if __name__ == '__main__':
    data = collect()
    target = Path(__file__).with_name('data.json')
    target.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Số liệu đã đối chiếu từ lab13.py: {target}')

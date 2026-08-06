@echo off
chcp 65001
cd /d "G:\我的雲端硬碟\Gpt理財\AI_Investment_HQ\09_給Claude\費半觀察站"
python scripts\update_tw.py
python scripts\calc_twii_gap_ma.py
pause
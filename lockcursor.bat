@echo off
set dc="Display Changer のパス"
set lockfile="%~dp0lockcursor.lock"
if exist %lockfile% (
  call %dc% -monitor="セカンド ディスプレイ" -ty=0
  del /q %lockfile%
) else (
  call %dc% -monitor="セカンド ディスプレイ" -ty=メイン ディスプレイの高さ
  echo -n "" > %lockfile%
)

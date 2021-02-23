```cmd
:: 源文件夹
set SrcDir=C:\Users\ispon\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
:: 临时文件夹
set TempDir=C:\Users\ispon\OneDrive\Pictures\config\temp
:: 目标文件夹
set PictureDir=C:\Users\ispon\OneDrive\Pictures\latest
:: 指定文件类型
set File=*

:: 拷贝图片进temp文件夹
if defined SrcDir cd /d "%SrcDir%"
for %%a in (%File%) do copy "%%~a" "%TempDir%\"

:: 修改临时文件夹中文件格式
if defined TempDir cd /d "%TempDir%"
for %%a in (%File%) do ren %%~a %%~a.png
for %%a in (%File%) do copy "%%~a" "%PictureDir%\"

:: 删除temp文件夹文件
if defined TempDir cd /d "%TempDir%"
del /f /s /q  %File%

:: 停止
pause
```
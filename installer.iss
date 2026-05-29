[Setup]
AppName=Mi Aplicacion
AppVersion=1.0
DefaultDirName={autopf}\MiAplicacion
DefaultGroupName=MiAplicacion
OutputDir=output
OutputBaseFilename=InstaladorMiAplicacion
Compression=lzma
SolidCompression=yes

LicenseFile=LICENSE.txt

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Mi Aplicacion"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Mi Aplicacion"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "Ejecutar aplicación"; Flags: nowait postinstall skipifsilent

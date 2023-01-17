# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['pyt_ganancias.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['psycopg2', 'socket', 'PyQt5', 'peewee', 'pandas', 'mx.DateTime', 'jinja2',  'pkg_resources.py2_warn', 'pkg_resources.markers', 'sip', 'xml.dom'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Payroll tools - Liquidador deducciones incrementadas',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='pyt_ganancias.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Payroll tools - Liquidador deducciones incrementadas')

# -*- mode: python -*-
a = Analysis(['orphan_content_remover.py'],
             pathex=['C:\\Users\\em\\Dropbox\\Dev\\projects\\bb-webdav-remove'],
             hiddenimports=['ssl'],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='orphan_content_remover.exe',
          debug=True,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='orphan_content_remover')

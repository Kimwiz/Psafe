# -*- mode: python -*-

block_cipher = None


a = Analysis(['PSafe.py'],
             pathex=['C:\\Users\\Neweinfeyn\\PycharmProjects\\Psafe'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='PSafe',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Python3.4\\Scripts\\irn.ico')

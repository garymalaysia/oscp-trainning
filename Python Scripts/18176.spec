# -*- mode: python -*-

block_cipher = None


a = Analysis(['18176.py'],
             pathex=['/root/Desktop/oscp-trainning/Python Scripts'],
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
          name='18176',
          debug=False,
          strip=False,
          upx=True,
          console=True )

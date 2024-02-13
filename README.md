# PDF Unlocker

このPythonスクリプトは、暗号化されたPDFファイルのパスワードを解除するためのものです。

## 導入
1. Pythonをインストールしてください https://www.python.org/downloads/
2. コマンドプロンプトから `pip install PyPDF2` を実行しPyPDF2をインストールしてください。
3. https://github.com/kotaooka/PDFUnlocker/releases から `PDFUnlocker.zip`をダウンロードしてください。
4. `PDFUnlocker.zip`を解答しお好きなディレクトリに配置します。

## 使用方法
1. `PDFUnlocker.bat`からPythonスクリプトを実行します。
2. ファイルダイアログが表示されるので、パスワードを解除したいPDFファイルを選択します。
3. スクリプトが自動的にパスワードを試行し、適切なパスワードが見つかった場合は、そのPDFファイルを復号化して保存します。

## 対応している文字列と桁数
`0123456789abcdefghijklmnopqrstuvwxyz` を組み合わせた1から8桁までの文字列

## 注意事項
このコードを使用する際は、必ず法律と倫理を遵守してください。
無断で他人のPDFファイルのパスワードを解除することは違法行為となります。

## ライセンス
Apache-2.0 license

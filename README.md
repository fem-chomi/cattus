# cattus
ソースコード自動生成ツール
ソースコードを自動生成するツールです。  
クラス定義とフィールド定義を入力すると指定されたプログラミング言語でソースコードを出力します。
本ツールはPython3上で動作します。  

#### 開発の背景

2013年からC#にてソースコードを自動生成ツールを継続的に開発していたが、
仕様追加のたびにソースコードが複雑化していき、
メンテナンス性が低下してしまった。  
また、設計書や説明書が整備されていないことから、開発者自身でも使用方法が分からない事態に陥った。  

さまざまな環境から実行できるPythonを選択し、一から再設計する。  

#### 対応プログラミング言語

C#製のソースコード自動生成ツールは廃止する。本ツールにて従来ツールと同等のコードを出力する。

- C#
- Python3
- SQL（SQLite3、SQL Server）

#### 対応予定のプログラミング言語

XCodeやVisual C++でも使用するかもしれないのでそのうち対応したい。

- Swift
- C++
- SQL（PostgreSQL、MySQL、Oracle）

#### 対応クラス

- DTO
- DTO Builder
- Entity
- Entity Builder
- DAO

#### 対応予定のクラス

- ValueObject
- SearchCondition
- SortCondition
- FilterCondition
- View
- MVVM
- Key
- Util

Comtrade-GRPC
===

Code for python used is mainly from  [dparrini/python-comtrade](https://github.com/dparrini/python-comtrade).

Just patch the code in `BinaryDatReader.parse` for parsing a little more efficiently.

### 1. Use `comtrade_grpc.py`

Basicly, the raw code in [dparrini/python-comtrade](https://github.com/dparrini/python-comtrade) is used like this:
```python
from comtrade import Comtrade

rec = Comtrade()
rec.load(cfg_file,dat_file)
```

With `Comtrade-GPRC`, you may write like this:
```python
from comtrade import Comtrade

# Passing a grpc_endpoint param will lead to using of parse() func in go with grpc

# 0ms

rec = comtrade_grpc.Comtrade(grpc_endpoint='localhost:50051')
rec.load(cfg_file,dat_file)

# 497.397ms

rec = comtrade_grpc.Comtrade()
rec.load(cfg_file,dat_file)

# 5809.528ms

```

### 2. Start grpc server

```bash
cd comtrade_grpc_server_go
go mod tidy
go run .
```

### 3. Make a docker image

Just build the `grpc-server.base.dockerfile`


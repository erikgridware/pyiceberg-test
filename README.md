# Setup
## 1. Setup your Unity Catalog server (Local only)
brew install openjdk\@17
# Follow zsh setup steps

git clone git@github.com:unitycatalog/unitycatalog.git
cd unitycatalog
build/sbt package
bin/start-uc-server

## 2. Run uv setup
```
uv sync
source .venv/bin/activate
```


# Running
Run `UC_ICEBERG_URI=localhost:8080/api/2.1/unity-catalog/iceberg python main.py`

# download model from huggingface
import os # Optional for faster downloading
from huggingface_hub import snapshot_download

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"

snapshot_download(
  repo_id = "Qwen/Qwen3-Embedding-0.6B",
  local_dir = "./models/Qwen3-Embedding-0.6B",
  # allow_patterns = ["*-Q8_0.gguf*"],
)
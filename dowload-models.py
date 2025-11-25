# download model from huggingface
import os # Optional for faster downloading
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"

from huggingface_hub import snapshot_download
snapshot_download(
  repo_id = "Qwen/Qwen3-8B-GGUF",
  local_dir = "./models/Qwen3-8B.gguf-Q8_0.gguf",
  allow_patterns = ["*-Q8_0.gguf*"],
)
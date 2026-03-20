# !pip install huggingface_hub hf_transfer
# download model from huggingface
import os # Optional for faster downloading
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

from huggingface_hub import snapshot_download
snapshot_download(
  repo_id = "unsloth/Qwen3-VL-4B-Instruct-GGUF",
  local_dir = "models/Qwen3-VL-4B-Instruct-GGUF",
  allow_patterns = ["*BF16*"],
)
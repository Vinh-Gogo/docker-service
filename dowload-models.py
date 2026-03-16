# !pip install huggingface_hub hf_transfer
# download model from huggingface
import os # Optional for faster downloading
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

from huggingface_hub import snapshot_download
snapshot_download(
  repo_id = "mradermacher/Huihui-Qwen3.5-27B-Claude-4.6-Opus-abliterated-i1-GGUF",
  local_dir = "models/Huihui-Qwen3.5-27B-Claude-4.6-Opus-abliterated-i1-GGUF",
  allow_patterns = ["*Q4_K_S*"],
)
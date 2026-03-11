# # download model from huggingface
# import os # Optional for faster downloading
# from huggingface_hub import snapshot_download

# os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"

# snapshot_download(
#   repo_id = "Qwen/Qwen3-Embedding-0.6B",
#   local_dir = "./models/Qwen3-Embedding-0.6B",
#   # allow_patterns = ["*-Q8_0.gguf*"],
# )

# !pip install huggingface_hub hf_transfer
# download model from huggingface
import os # Optional for faster downloading
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

# from huggingface_hub import snapshot_download
# snapshot_download(
#   repo_id = "unsloth/Qwen3-30B-A3B-GGUF",
#   local_dir = "unsloth_Qwen3-30B-A3B-GGUF",
#   allow_patterns = ["*Q6_K_XL*"],
# )

from huggingface_hub import snapshot_download
snapshot_download(
  repo_id = "unsloth/Qwen3.5-35B-A3B-GGUF",
  local_dir = "unsloth/Qwen3.5-35B-A3B-GGUF",
  allow_patterns = ["*UD-IQ4_NL*"],
)
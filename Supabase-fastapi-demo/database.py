import os
from dotenv import load_dotenv
from supabase import Client , create_client

# ================
# Loading URLs
# ================
load_dotenv()

# ==================================
# Loading the URL of SUPABASE
# =================================
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# ============================
# Validate Configuration
#=============================
if not supabase_url or not supabase_url:
    raise RuntimeError("SUPABASE_URL or SUPABASE_KEY are not defined in .env")

# ====================
# Create a client
# ====================
supabase : Client = create_client(supabase_url,supabase_key)


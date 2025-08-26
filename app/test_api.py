import os
import traceback

# Test if environment variables are set
print("Environment check:")
print(f"GROQ_API_KEY: {'SET' if os.getenv('GROQ_API_KEY') else 'NOT SET'}")
print()

try:
    # Import your function
    from app.core.ai_agent import get_response_from_ai_agents
    print("✅ Successfully imported get_response_from_ai_agents")
    
    # Test the function directly
    print("🧪 Testing AI agent function...")
    
    response = get_response_from_ai_agents(
        model_name="llama3-70b-8192",
        query=["Hello, how are you?"],
        allow_search=False,
        system_prompt="You are a helpful assistant"
    )
    
    print(f"✅ Success! Response: {response}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    traceback.print_exc()
    
except Exception as e:
    print(f"❌ Function error: {e}")
    print(f"Error type: {type(e).__name__}")
    traceback.print_exc()
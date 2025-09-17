import from mtllm.llms { Gemini }
import from supabase { create_client }
import from sentence_transformers { SentenceTransformer }
import os;
import from dotenv { load_dotenv }
import time;

glob llm = Gemini(model_name="gemini-2.5-flash");

def get_embedding(text: str) -> list {
    load_dotenv();
    SUPABASE_URL = os.environ[ 'SUPABASE_URL' ];
    SUPABASE_KEY = os.environ[ 'SUPABASE_KEY' ];
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY);
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2');

    emb = model.encode([text])[0];
    response = supabase.rpc('match_documents', {'query_embedding' : emb.tolist() , 'match_count' : 5 }).execute();
    
    contents = [];
    for result in response.data { 
        contents.append(result[ 'content' ]); 
    }
    return contents;
}

"""Generate the response for the given query where list of content for the response should be retrieved by executing the get_embedding() tool.
    Content return as a list format by get_embedding().
"""
def generate_response(text: str) -> str by llm(method="ReAct", tools=[get_embedding]);

walker Supervisor {
    has query: str= "";

    obj __specs__{
        static has auth: bool = False;
    }
    can start with `root entry {
        print("Starting Supervisor...");
        # self.query = "code example of how to use the 'disengage' command?";
        # response = get_embedding(self.query);
        response = generate_response(self.query);
        print(response);
        report{"ChatBot":response};
    }
}

# with entry {
#     Supervisor(query="If I need to discontinue a walker at some point, what should I do?") spawn root;
# }
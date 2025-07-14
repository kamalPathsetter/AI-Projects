from flask import Flask,render_template,request,session,redirect,url_for
from app.components.retriever import create_chain, get_context_from_query
from dotenv import load_dotenv
import os


load_dotenv()
HF_TOKEN = os.environ.get("HF_TOKEN")

app = Flask(__name__)
app.secret_key = os.urandom(24)
load_dotenv()


@app.route("/" , methods=["GET","POST"])
def index():
    if "messages" not in session:
        session["messages"]=[]

    if request.method=="POST":
        user_input = request.form.get("prompt")

        if user_input:
            messages = session["messages"]
            messages.append({"role" : "user" , "content":user_input})
            session["messages"] = messages

            try:
                chain = create_chain()
                if chain is None:
                    raise Exception("Chain could not be created (LLM issue)")
                
                context = get_context_from_query(user_input)
                
                chat_history = ""
                for msg in messages[:-1]:  # Exclude the current user message
                    chat_history += f"{msg['role'].capitalize()}: {msg['content']}\n"
                
                response = chain.invoke({
                    "question": user_input,
                    "context": context,
                    "chat_history": chat_history
                })
                result = response.get("text", "No response")

                messages.append({"role" : "assistant" , "content" : result})
                session["messages"] = messages

            except Exception as e:
                error_msg = f"Error : {str(e)}"
                return render_template("index.html" , messages = session["messages"] , error = error_msg)
            
        return redirect(url_for("index"))
    return render_template("index.html" , messages=session.get("messages" , []))

@app.route("/clear")
def clear():
    session.pop("messages" , None)
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(host="0.0.0.0" , port=5000 , debug=False , use_reloader = False)
## How RAG Works

Pure Prompt only does generation. In case of RAG, model did not learn
any new data via fine-tuning or retraining.

# Retrieval
Where you will search private knowledge w/respect to query response and get relevant chunks of information

# Augmentation
Augment the prompt where you plug these chunks and the questions into an prompt template 

# Generation
Send prompt template to LLM and generate the perfect answer.
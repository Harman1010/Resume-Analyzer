## Resume Analyzer

This project is an AI-powered ATS (Applicant Tracking System) evaluation and resume enhancement platform that analyzes resumes and job descriptions using NLP and transformer-based semantic embeddings.

The system computes ATS compatibility scores dynamically by combining semantic similarity, skill-level matching, keyword analysis, and critical requirement evaluation. It also identifies missing skills and generates resume improvement suggestions to help candidates improve job-role alignment.

##Working

The project follows a hybrid NLP pipeline architecture.

• Resume and Job Description inputs are processed from PDF or text format.

• Sentence Transformers are used to generate semantic embeddings for contextual understanding.

• KeyBERT and skill ontology-based extraction are used to identify important technical and non-technical skills.

• TF-IDF and cosine similarity are used for keyword-based ATS matching.

• A weighted ATS scoring engine combines semantic similarity, skill matching, keyword overlap, and critical skill penalties.

• Missing skills and weak alignment areas are analyzed to generate rule-guided resume improvement suggestions.

##Tech Stack

• Python
• Sentence Transformers
• KeyBERT
• Scikit-learn
• TF-IDF Vectorizer
• Cosine Similarity
• PDFPlumber
• Gradio

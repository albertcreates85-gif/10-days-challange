# **Semantic Auditor: Intelligent Text Weighting & Analysis**

The **Semantic Auditor** is a high-level text analysis tool designed to bridge the gap between raw data parsing and cognitive synthesis. Unlike traditional NLP methods that rely on simple keyword frequency, this project leverages the **Google Gemini 3 Flash** engine to perform semantic evaluation, assigning mathematical "importance weights" to individual lines of text to identify high-density information.

---

### **Core Functionality**
This application processes structured or unstructured text files, validates their integrity, and performs a multi-stage analysis:
1.  **Line-by-Line Weighting:** Evaluates the informational significance of every sentence on a scale of 1–10.
2.  **Key Highlight Extraction:** Distills the core narrative into structured JSON-formatted highlights.
3.  **Executive Summary:** Generates a concise, high-level overview of the entire dataset.
4.  **Automated Reporting:** Exports the full analysis into a clean, portable text format for stakeholders.

---

### **Technical Stack**
* **Language:** Python 3.10+
* **Engine:** Google Gemini 3 Flash API
* **Environment:** Google Colab
* **Interface:** IPython Widgets (Form-based UI)
* **Data Handling:** JSON & OS-level File I/O

---

### **Architectural Workflow**

1.  **Ingestion:** The system accepts `.txt` files with strict size validation (1KB–10KB) to ensure high-speed processing and token efficiency.
2.  **Processing:**
    * The script parses the file into a list of strings.
    * A prompt-engineered payload is sent to the Gemini API, requesting a mapping of indices to importance weights.
    * The model returns a JSON object which the script parses to visualize data density.
3.  **Synthesis:** The API identifies the "Golden Sentences" for highlights while simultaneously condensing the narrative into a summary.
4.  **Output:** Results are displayed via an interactive notebook interface and saved to a local file.

---

### **Key Features**

#### **1. Intelligent Information Density Mapping**
By assigning weights to each line, the auditor allows users to quickly scan large documents and identify exactly where the most critical information resides, effectively acting as a "heat map" for text.

#### **2. API-First Architecture**
By offloading the NLP heavy-lifting to Google's infrastructure, the tool maintains a zero-footprint local environment, making it highly portable and easy to deploy without managing heavy machine-learning dependencies.

#### **3. Structured Output**
The project prioritizes data integrity by forcing the LLM to return structured JSON, ensuring that the highlights and weights can be integrated into larger data pipelines or SQL databases in the future.

---

### **How to Deploy**
1.  **Secure Credentials:** Store your `GOOGLE_API_KEY` in the Google Colab "Secrets" sidebar.
2.  **Environment Setup:** Run the notebook to install the `google-generativeai` library.
3.  **Execution:** Run the UI cell, upload a document, and trigger the **Analyze** function.
4.  **Reporting:** Access the `analysis_results.txt` file generated in the local directory.

---

**Developed with precision for high-level data analysis.**

**Signed,** **Mayank**

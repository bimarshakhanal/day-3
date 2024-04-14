#ref: https://refactoring.guru/design-patterns/builder/python/example

from abc import ABC, abstractmethod

class DocumentBuilder(ABC):
    @abstractmethod
    def set_title(self, title):
        pass
    
    @abstractmethod
    def add_heading(self, heading):
        pass
    
    @abstractmethod
    def add_paragraph(self, paragraph):
        pass
    
    @abstractmethod
    def get_document(self):
        pass

class PDFDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = {}

    def set_title(self, title):
        self.document['title'] = title
    
    def add_heading(self, heading):
        if 'headings' not in self.document:
            self.document['headings'] = []
        self.document['headings'].append(heading)
    
    def add_paragraph(self, paragraph):
        if 'paragraphs' not in self.document:
            self.document['paragraphs'] = []
        self.document['paragraphs'].append(paragraph)
    
    def get_document(self):
        return self.document

class HTMLDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = "<html><head><title></title></head><body>"
    
    def set_title(self, title):
        self.document += f"<h1>{title}</h1>"
    
    def add_heading(self, heading):
        self.document += f"<h2>{heading}</h2>"
    
    def add_paragraph(self, paragraph):
        self.document += f"<p>{paragraph}</p>"
    
    def get_document(self):
        return self.document + "</body></html>"

class PlainTextDocumentBuilder(DocumentBuilder):
    def __init__(self):
        self.document = ""

    def set_title(self, title):
        self.document += f"{title}\n\n"
    
    def add_heading(self, heading):
        self.document += f"{heading}\n"
    
    def add_paragraph(self, paragraph):
        self.document += f"{paragraph}\n\n"
    
    def get_document(self):
        return self.document

class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def build_document(self, title, headings, paragraphs):
        self.builder.set_title(title)
        for heading in headings:
            self.builder.add_heading(heading)
        for paragraph in paragraphs:
            self.builder.add_paragraph(paragraph)
        return self.builder.get_document()


# Define document contents:
title = "Sample Document"
headings = ["Introduction", "Main Content", "Conclusion"]
paragraphs = ["This is the introduction paragraph.",
              "This is the main content paragraph.",
              "This is the conclusion paragraph."]

# different document instance of each document type
pdf_builder = PDFDocumentBuilder()
html_builder = HTMLDocumentBuilder()
plain_text_builder = PlainTextDocumentBuilder()

# director instance to build document step by step
director = DocumentDirector(pdf_builder)
pdf_document = director.build_document(title, headings, paragraphs)
print("PDF Document:")
print(pdf_document)

director = DocumentDirector(html_builder)
html_document = director.build_document(title, headings, paragraphs)
print("\nHTML Document:")
print(html_document)

director = DocumentDirector(plain_text_builder)
plain_text_document = director.build_document(title, headings, paragraphs)
print("\nPlain Text Document:")
print(plain_text_document)

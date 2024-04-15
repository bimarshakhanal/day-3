# ref: https://refactoring.guru/design-patterns/builder/python/example

from abc import ABC, abstractmethod


class DocumentBuilder(ABC):
    '''Abstract base class representing a document builder.'''

    @abstractmethod
    def set_title(self, title):
        '''Set the title of the document.'''

    @abstractmethod
    def add_heading(self, heading):
        '''Add a heading to the document.'''

    @abstractmethod
    def add_paragraph(self, paragraph):
        '''Add a paragraph to the document.'''

    @abstractmethod
    def get_document(self):
        '''Get the final document created by the builder.'''


class PDFDocumentBuilder(DocumentBuilder):
    '''Concrete builder class for creating PDF documents.'''

    def __init__(self):
        '''Initialize a PDF document builder.'''
        self.document = {}

    def set_title(self, title):
        '''Set the title of the PDF document.'''
        self.document['title'] = title

    def add_heading(self, heading):
        '''Add a heading to the PDF document.'''
        if 'headings' not in self.document:
            self.document['headings'] = []
        self.document['headings'].append(heading)

    def add_paragraph(self, paragraph):
        '''Add a paragraph to the PDF document.'''
        if 'paragraphs' not in self.document:
            self.document['paragraphs'] = []
        self.document['paragraphs'].append(paragraph)

    def get_document(self):
        '''Get the final PDF document.'''
        return self.document


class HTMLDocumentBuilder(DocumentBuilder):
    '''Concrete builder class for creating HTML documents.'''

    def __init__(self):
        '''Initialize an HTML document builder.'''
        self.document = "<html><head><title></title></head><body>"

    def set_title(self, title):
        '''Set the title of the HTML document.'''
        self.document += f"<h1>{title}</h1>"

    def add_heading(self, heading):
        '''Add a heading to the HTML document.'''
        self.document += f"<h2>{heading}</h2>"

    def add_paragraph(self, paragraph):
        '''Add a paragraph to the HTML document.'''
        self.document += f"<p>{paragraph}</p>"

    def get_document(self):
        '''Get the final HTML document.'''
        return self.document + "</body></html>"


class PlainTextDocumentBuilder(DocumentBuilder):
    '''Concrete builder class for creating plain text documents.'''

    def __init__(self):
        '''Initialize a plain text document builder.'''
        self.document = ""

    def set_title(self, title):
        '''Set the title of the plain text document.'''
        self.document += f"{title}\n\n"

    def add_heading(self, heading):
        '''Add a heading to the plain text document.'''
        self.document += f"{heading}\n"

    def add_paragraph(self, paragraph):
        '''Add a paragraph to the plain text document.'''
        self.document += f"{paragraph}\n\n"

    def get_document(self):
        '''Get the final plain text document.'''
        return self.document


class DocumentDirector:
    '''Class responsible for directing the construction of documents using a builder.'''

    def __init__(self, builder):
        '''Initialize the document director with a builder.'''
        self.builder = builder

    def build_document(self, title, headings, paragraphs):
        '''Build a document with the given title, headings, and paragraphs.'''
        self.builder.set_title(title)
        for heading in headings:
            self.builder.add_heading(heading)
        for paragraph in paragraphs:
            self.builder.add_paragraph(paragraph)
        return self.builder.get_document()


# Define document contents:
TITLE = "Sample Document"
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
pdf_document = director.build_document(TITLE, headings, paragraphs)
print("PDF Document:")
print(pdf_document)

director = DocumentDirector(html_builder)
html_document = director.build_document(TITLE, headings, paragraphs)
print("\nHTML Document:")
print(html_document)

director = DocumentDirector(plain_text_builder)
plain_text_document = director.build_document(TITLE, headings, paragraphs)
print("\nPlain Text Document:")
print(plain_text_document)

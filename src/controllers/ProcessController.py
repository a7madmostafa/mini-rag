import os
from .BaseController import BaseController
from .ProjectController import ProjectController
from models import ProcessEnums
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class ProcessController(BaseController):
    def __init__(self, project_id: str):
        
        super().__init__()

        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)

    def get_file_extension(self, file_id: str) -> str:
        """
        Get the file extension from the given file_id.

        Parameters
        ----------
        file_id : str
            The file_id to get the extension from.

        Returns
        -------
        str
            The file extension (e.g., .txt, .pdf).
        """
        return os.path.splitext(file_id)[-1]
    
    def get_file_loader(self, file_id: str):

        """
        Get the file loader based on the given file_id.

        Parameters
        ----------
        file_id : str
            The file_id to get the loader from.

        Returns
        -------
        langchain_community.document_loaders.TextLoader or langchain_community.document_loaders.PyMuPDFLoader
            The file loader based on the file extension (txt or pdf).

        Raises
        ------
        ValueError
            If the file extension is not supported (txt or pdf).
        """
        file_extension = self.get_file_extension(file_id).lower()
        file_path = os.path.join(self.project_path, file_id)

        if file_extension == ProcessEnums.TXT.value:
            return TextLoader(file_path, encoding='utf-8')

        elif file_extension == ProcessEnums.PDF.value:
            return PyMuPDFLoader(file_path)
        
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
    def get_file_content(self, file_id: str):
        """
        Get the content of the file based on the given file_id.

        Parameters
        ----------
        file_id : str
            The file_id to get the content from.

        Returns
        -------
        list of langchain_community.document_loaders.Document
            The file content as a list of Document objects.
            One Document is one file

        Raises
        ------
        ValueError
            If the file extension is not supported (txt or pdf).
        """
        loader = self.get_file_loader(file_id)
        documents = loader.load()
        return documents
    
    def process_file_content(self, file_id: str, chunk_size: int, overlap: int):
        """
        Process the content of the file based on the given file_id.

        Parameters
        ----------
        file_id : str
            The file_id to process the content from.
        chunk_size : int
            The size of each text chunk.
        overlap : int
            The size of the overlap between chunks.

        Returns
        -------
        list of langchain_community.document_loaders.Document
            The processed file content as a list of Document objects.
            One Document is one chunk

        Notes
        -----
        This method uses the RecursiveCharacterTextSplitter to split the file content into chunks with the given chunk size and overlap.
        """
        documents = self.get_file_content(file_id)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            length_function=len,
        )

        file_content_texts = [ doc.page_content for doc in documents ]
        file_content_metadata = [ doc.metadata for doc in documents ]

        chunks = text_splitter.create_documents(file_content_texts, file_content_metadata)

        return chunks
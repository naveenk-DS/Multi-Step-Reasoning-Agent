class LLMBase : 
    """
    Base class for all LLM Provider.
    """
    
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Subclasses must implement generate()")
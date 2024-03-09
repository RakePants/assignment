import logging

from src.utils.interfaces import interface

if __name__ == "__main__":
    server_port = 7860

    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info(f"Interface available at http://localhost:{server_port}/")

    interface.launch(server_name="0.0.0.0", server_port=server_port, show_error=True)

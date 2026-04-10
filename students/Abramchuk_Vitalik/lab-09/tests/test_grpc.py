import grpc
from grpc_notes.notes_pb2 import CreateNoteRequest, GetNoteRequest
from grpc_notes import notes_pb2_grpc
from grpc_notes.server import serve
import threading


def start_server():
    serve()


def test_create_and_get():
    threading.Thread(target=start_server, daemon=True).start()

    channel = grpc.insecure_channel("localhost:50051")
    client = notes_pb2_grpc.NotesServiceStub(channel)

    created = client.CreateNote(
        CreateNoteRequest(
            notebook_id="1",
            author_id="1",
            content="Test"
        )
    )

    note = client.GetNote(
        GetNoteRequest(note_id=created.note_id)
    )

    assert note.content == "Test"
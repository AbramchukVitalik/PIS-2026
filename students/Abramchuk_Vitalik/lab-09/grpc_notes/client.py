# grpc/client.py
import grpc
from grpc_notes.notes_pb2 import CreateNoteRequest, GetNoteRequest, StreamNotesRequest
from grpc_notes import notes_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    client = notes_pb2_grpc.NotesServiceStub(channel)

    # Create note
    response = client.CreateNote(
        CreateNoteRequest(
            notebook_id="1",
            author_id="1",
            content="Hello gRPC"
        )
    )

    print("Created:", response.note_id)

    # Get note
    note = client.GetNote(
        GetNoteRequest(note_id=response.note_id)
    )

    print("Fetched:", note)

    # Stream notes
    for n in client.StreamNotes(
        StreamNotesRequest(notebook_id="1")
    ):
        print("STREAM:", n)


if __name__ == "__main__":
    run()
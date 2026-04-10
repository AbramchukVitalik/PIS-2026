# grpc/server.py
from concurrent import futures
import grpc
from grpc_notes.notes_pb2 import CreateNoteResponse, NoteResponse
from grpc_notes import notes_pb2_grpc

from services.notes_service import NotesService

service = NotesService()

class NotesServicer(notes_pb2_grpc.NotesServiceServicer):

    def CreateNote(self, request, context):
        note = service.create_note(
            request.notebook_id,
            request.author_id,
            request.content
        )

        return CreateNoteResponse(note_id=note["note_id"])

    def GetNote(self, request, context):
        note = service.get_note(request.note_id)

        if not note:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return NoteResponse()

        return NoteResponse(**note)

    def StreamNotes(self, request, context):
        for note in service.stream_notes(request.notebook_id):
            yield NoteResponse(**note)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_pb2_grpc.add_NotesServiceServicer_to_server(
        NotesServicer(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
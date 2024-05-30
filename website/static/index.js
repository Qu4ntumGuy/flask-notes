const deleteNote = (noteId) => {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });

  //   const noteId = document.getElementById("note-id").value;
  //   fetch(`/api/notes/${noteId}`, {
  //     method: "DELETE",
  //   }).then(() => {
  //     window.location.href = "/";
  //   });
};

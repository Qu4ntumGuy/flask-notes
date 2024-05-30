const deleteNote = (noteId) => {
  //   fetch(`/api/notes/${noteId}`, {
  //     method: "DELETE",
  //   }).then(() => {
  //     window.location.href = "/";
  //   });

  const noteId = document.getElementById("note-id").value;
  fetch(`/api/notes/${noteId}`, {
    method: "DELETE",
  }).then(() => {
    window.location.href = "/";
  });
};

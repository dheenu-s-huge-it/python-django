document.addEventListener("DOMContentLoaded", () => {
  let timeout = null;

  const input = document.getElementById("searchInput");
  const form = document.getElementById("searchForm");
  const categorySelect = document.querySelector('select[name="category"]');

  if (!input || !form) return;

  input.focus();

  const val = input.value;
  input.value = "";
  input.value = val;

  categorySelect.addEventListener('change', () => {
        searchForm.submit();
    });

  input.addEventListener("keydown", () => {
    clearTimeout(timeout);

    timeout = setTimeout(() => {
      form.submit();
    }, 400);
  });
});

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

  document.addEventListener('DOMContentLoaded', function() {
    const userInfo = document.querySelector('.user-info');
    
    if (userInfo) {
      userInfo.addEventListener('click', function(e) {
        // Prevent the click from bubbling up if you click the button itself
        if (e.target.tagName !== 'BUTTON') {
          this.classList.toggle('active');
        }
      });

      // Close the dropdown if clicking anywhere else on the screen
      document.addEventListener('click', function(e) {
        if (!userInfo.contains(e.target)) {
          userInfo.classList.remove('active');
        }
      });
    }
  });
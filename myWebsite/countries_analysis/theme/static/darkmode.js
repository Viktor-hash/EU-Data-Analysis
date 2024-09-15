// Check and apply the user's stored preference or the system preference on page load
if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
  
  // User actions to explicitly choose themes
  function toggleTheme(isDark) {
    localStorage.theme = isDark ? 'dark' : 'light'; // Save preference
    document.documentElement.classList.toggle('dark', isDark);
  }
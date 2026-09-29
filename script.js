function formatText(command) {
  document.execCommand(command, false, null);
}

// For newer browsers that don't support execCommand
if (typeof document.queryCommandSupported === 'function' && !document.queryCommandSupported('bold')) {
  document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.toolbar button');
    buttons.forEach(button => {
      button.addEventListener('click', function() {
        const command = this.getAttribute('data-command');
        document.execCommand(command, false, null);
      });
    });
  });
}
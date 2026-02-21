// Layer chip selection
const chips = document.querySelectorAll('.chip');
chips.forEach((chip, idx) => {
  chip.addEventListener('click', () => {
    chips.forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
  });
});

// Key glow effect
const keys = document.querySelectorAll('.key-btn');
keys.forEach((key) => {
  key.addEventListener('touchstart', () => {
    key.classList.add('active');
  });
  key.addEventListener('touchend', () => {
    key.classList.remove('active');
  });
  key.addEventListener('mousedown', () => {
    key.classList.add('active');
  });
  key.addEventListener('mouseup', () => {
    key.classList.remove('active');
  });
  key.addEventListener('mouseleave', () => {
    key.classList.remove('active');
  });
});

// Volume slider
const slider = document.getElementById('volume-slider');
const sliderValue = document.getElementById('slider-value');
if (slider && sliderValue) {
  slider.addEventListener('input', () => {
    sliderValue.textContent = slider.value + '%';
  });
}

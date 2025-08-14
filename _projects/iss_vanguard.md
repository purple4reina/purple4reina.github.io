---
layout: default
permalink: /projects/iss-vanguard
bootstrap: true
---

# ISS Vanguard: _Dice Probability Calculator_

<div class="container">
  <div class="row">
    <div class="col">
      <label for="dice-input" class="form-label">Dice Input</label>
      <div class="input-group mb-3" id="dice-input">
        <select class="form-select" id="dice-color-select">
          <option value="" selected disabled>Color...</option>
          <option value="red">Red</option>
          <option value="green">Green</option>
          <option value="blue">Blue</option>
        </select>
        <select class="form-select" id="dice-icon-placeholder">
          <option selected disabled>Icon...</option>
        </select>
        <select class="form-select" id="dice-icon-select-red" hidden>
          <option value="" selected disabled>Icon...</option>
          <option value="basic">Basic</option>
          <option value="strength">Strength</option>
          <option value="shield">Shield</option>
          <option value="pickaxe">Pick Axe</option>
          <option value="vanguard">Vanguard</option>
        </select>
        <select class="form-select" id="dice-icon-select-green" hidden>
          <option value="" selected disabled>Icon...</option>
          <option value="basic">Basic</option>
          <option value="compass">Compass</option>
          <option value="eyeball">Eyeball</option>
          <option value="dna">DNA</option>
          <option value="vanguard">Vanguard</option>
        </select>
        <select class="form-select" id="dice-icon-select-blue" hidden>
          <option value="" selected disabled>Icon...</option>
          <option value="basic">Basic</option>
          <option value="wrench">Wrench</option>
          <option value="computer">Computer</option>
          <option value="science">Science</option>
          <option value="vanguard">Vanguard</option>
        </select>
        <button class="btn btn-outline-secondary" type="button" id="add-die-button" disabled>
          <i class="bi bi-plus-lg"></i>Add Die
        </button>
      </div>
      <div id="dice-list" class="list-group">
        <!-- Dice will be added here dynamically -->
      </div>
    </div>
  </div>
</div>

<script>
  const diceColorSelect = document.getElementById('dice-color-select');
  const diceIconPlaceholder = document.getElementById('dice-icon-placeholder');
  const diceIconSelectRed = document.getElementById('dice-icon-select-red');
  const diceIconSelectGreen = document.getElementById('dice-icon-select-green');
  const diceIconSelectBlue = document.getElementById('dice-icon-select-blue');
  const addDieButton = document.getElementById('add-die-button');
  const diceList = document.getElementById('dice-list');

  function updateDiceColor(event) {
    selectedColor = event.target.value;
    diceIconPlaceholder.hidden = true;
    diceIconSelectRed.hidden = selectedColor === 'green' || selectedColor === 'blue';
    diceIconSelectGreen.hidden = selectedColor !== 'green';
    diceIconSelectBlue.hidden = selectedColor !== 'blue';
    diceIconSelectRed.disabled = false;

    diceIconSelectRed.value = diceIconSelectGreen.value = diceIconSelectBlue.value = '';
    addDieButton.disabled = true;
  }

  function updateDiceIcon(event) {
    addDieButton.disabled = false;
  }

  function addDie() {
    const selectedColor = diceColorSelect.value;
    let selectedIcon;

    if (selectedColor === 'red') {
      selectedIcon = diceIconSelectRed.value;
    } else if (selectedColor === 'green') {
      selectedIcon = diceIconSelectGreen.value;
    } else if (selectedColor === 'blue') {
      selectedIcon = diceIconSelectBlue.value;
    }

    if (selectedIcon) {
      const dieItem = document.createElement('div');
      dieItem.className = 'list-group-item d-flex justify-content-between align-items-center';
      dieItem.textContent = `${selectedColor.charAt(0).toUpperCase() + selectedColor.slice(1)} ${selectedIcon.charAt(0).toUpperCase() + selectedIcon.slice(1)}`;
      diceList.appendChild(dieItem);

      diceColorSelect.value = '';
      diceIconPlaceholder.hidden = false;
      diceIconSelectRed.hidden = true;
      diceIconSelectGreen.hidden = true;
      diceIconSelectBlue.hidden = true;
      addDieButton.disabled = true;
    }
  }

  diceColorSelect.addEventListener('change', updateDiceColor);
  diceIconSelectRed.addEventListener('change', updateDiceIcon);
  diceIconSelectGreen.addEventListener('change', updateDiceIcon);
  diceIconSelectBlue.addEventListener('change', updateDiceIcon);
  addDieButton.addEventListener('click', addDie);
</script>

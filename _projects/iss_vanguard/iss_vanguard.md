---
layout: default
permalink: /projects/iss-vanguard
bootstrap: true
---

# ISS Vanguard: _Dice Probability Calculator_

<div class="container">
  <div class="row">
    <div class="col" style="margin-bottom: 20px;">
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
      <div id="dice-list" class="list-group"></div>
    </div>
  </div>

  <div class="row">
    <div class="col" style="margin-bottom: 20px;">
      <div class="row">
        <div class="col">
          <label for="fails-input" class="form-label">Fail Conditions</label>
        </div>
        <div class="col">
          <div class="btn-group btn-group-sm" role="group">
            <input type="radio" class="btn-check" name="fail-and-or" id="and" disabled>
            <label class="btn btn-outline-secondary" for="and">And</label>
            <input type="radio" class="btn-check" name="fail-and-or" id="or" checked>
            <label class="btn btn-outline-secondary" for="or">Or</label>
          </div>
        </div>
      </div>
      <div class="input-group mb-3" id="fails-input">
        <select class="form-select" id="fails-select">
          <option value="" selected disabled>Select...</option>
          <option value="bang">Bang</option>
        </select>
        <button class="btn btn-outline-secondary" type="button" id="add-fail-button" disabled>
          <i class="bi bi-plus-lg"></i>Add Fail
        </button>
      </div>
      <div id="fails-list" class="list-group"></div>
    </div>
  </div>

  <div class="row" style="margin-bottom: 20px;">
    <div class="col">
      <button class="btn btn-outline-secondary" type="button" id="calculate-button" disabled>
        <i class="bi bi-calculator"></i> Calculate
      </button>
    </div>
  </div>

  <div class="row">
    <div class="col">
      <hr class="border border-secondary border-1" />
      <h5>Results</h5>
      <div id="results-bar" hidden>
        <div class="progress-stacked" style="height: 24px">
          <div class="progress" id="results-bar-fail" role="progressbar" style="height: 24px">
            <div class="progress-bar bg-danger"></div>
          </div>
          <div class="progress opacity-0" id="results-bar-none" role="progressbar" style="height: 24px">
            <div class="progress-bar"></div>
          </div>
          <div class="progress" id="results-bar-success" role="progressbar" style="height: 24px">
            <div class="progress-bar bg-success"></div>
          </div>
        </div>
        <div class="col justify-content-between d-flex" style="margin: 5px">
          <span id="results-bar-fail-text"></span>
          <span id="results-bar-success-text"></span>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  // Add Dice
  const diceColorSelect = document.getElementById('dice-color-select');
  const diceIconPlaceholder = document.getElementById('dice-icon-placeholder');
  const diceIconSelectRed = document.getElementById('dice-icon-select-red');
  const diceIconSelectGreen = document.getElementById('dice-icon-select-green');
  const diceIconSelectBlue = document.getElementById('dice-icon-select-blue');
  const addDieButton = document.getElementById('add-die-button');
  const diceList = document.getElementById('dice-list');

  const dice = [];

  // Add Fail Conditions
  const failsSelect = document.getElementById('fails-select');
  const addFailButton = document.getElementById('add-fail-button');
  const failsList = document.getElementById('fails-list');

  const fails = [];

  // Calculate
  const calculateButton = document.getElementById('calculate-button');
  const resultsBar = document.getElementById('results-bar');
  const resultsBarFail = document.getElementById('results-bar-fail');
  const resultsBarNone = document.getElementById('results-bar-none');
  const resultsBarSuccess = document.getElementById('results-bar-success');
  const resultsBarFailText = document.getElementById('results-bar-fail-text');
  const resultsBarSuccessText = document.getElementById('results-bar-success-text');

  const backendUrl =
    {%- if site.env == "dev" -%}
      'http://localhost:8000'
    {%- else -%}
      'https://6ej4pejufnxacafmtzeu7u5rsa0wgavk.lambda-url.us-west-2.on.aws'
    {%- endif %};

  // Add Dice

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

    if (!selectedIcon) {
      return;
    }

    dice.push({ color: selectedColor, icon: selectedIcon });

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
    calculateButton.disabled = false;
  }

  // Add Fail Conditions

  function updateFails(event) {
    addFailButton.disabled = event.target.value === '';
  }

  function addFails(event) {
    const selectedFail = failsSelect.value;

    fails.push(selectedFail);

    const failItem = document.createElement('div');
    failItem.className = 'list-group-item d-flex justify-content-between align-items-center';
    failItem.textContent = selectedFail.charAt(0).toUpperCase() + selectedFail.slice(1);
    failsList.appendChild(failItem);

    failsSelect.value = '';
    addFailButton.disabled = true;
  }

  // Calculate

  async function calculate() {
    if (dice.length === 0) {
      return;
    }

    resultsBar.hidden = true;

    const resp = await fetch(backendUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          dice: dice,
          fails: fails,
          failCondition: document.querySelector('input[name="fail-and-or"]:checked').id,
        })
      })
      .then(response => {
        const body = response.json().then();
        return body;
      })
      .catch(error => {
        console.error('Error:', error);
        return { failure_probability: 0, success_probability: 0 };
      });
    console.log('Response:', resp);

    const failPercent = resp.failure_probability * 100;
    const successPercent = resp.success_probability * 100;
    const nonePercent = 100 - (failPercent + successPercent);

    resultsBarFail.style.width = `${failPercent}%`;
    resultsBarNone.style.width = `${nonePercent}%`;
    resultsBarSuccess.style.width = `${successPercent}%`;
    resultsBarFailText.textContent = `${failPercent}% Fail`;
    resultsBarSuccessText.textContent = `${successPercent}% Success`;
    resultsBar.hidden = false;
  }

  // Add Dice
  diceColorSelect.addEventListener('change', updateDiceColor);
  diceIconSelectRed.addEventListener('change', updateDiceIcon);
  diceIconSelectGreen.addEventListener('change', updateDiceIcon);
  diceIconSelectBlue.addEventListener('change', updateDiceIcon);
  addDieButton.addEventListener('click', addDie);

  // Add Fail Conditions
  failsSelect.addEventListener('change', updateFails);
  addFailButton.addEventListener('click', addFails);

  // Calculate
  calculateButton.addEventListener('click', calculate);
</script>

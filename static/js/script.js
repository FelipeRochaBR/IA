function atualizarCampos() {
  const metodoSelecionado = document.querySelector(
    'input[name="metodo"]:checked'
  );

  if (!metodoSelecionado) {
    return;
  }

  const valorSelecionado = metodoSelecionado.value;

  const inicioBox = document.getElementById("inicioBox");
  const objetivoBox = document.getElementById("objetivoBox");
  const limite = document.getElementById("limite");

  if (
    valorSelecionado === "amplitude" ||
    valorSelecionado === "bidirecional" ||
    valorSelecionado === "profundidade"
  ) {
    inicioBox.classList.remove("hidden");
    objetivoBox.classList.remove("hidden");
    limite.classList.add("hidden");
  } else {
    inicioBox.classList.remove("hidden");
    objetivoBox.classList.remove("hidden");
    limite.classList.remove("hidden");
  }
}

document.querySelectorAll('input[name="metodo"]').forEach((radio) => {
  radio.addEventListener("change", atualizarCampos);
});

atualizarCampos();

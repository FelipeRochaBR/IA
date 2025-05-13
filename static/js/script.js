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
    valorSelecionado === "profundidade_limitada"
  ) {
    inicioBox.classList.remove("hidden");
    objetivoBox.classList.remove("hidden");
    limite.classList.remove("hidden");
  } else {
    inicioBox.classList.remove("hidden");
    objetivoBox.classList.remove("hidden");
    limite.classList.add("hidden");
  }
}

document.querySelectorAll('input[name="metodo"]').forEach((radio) => {
  radio.addEventListener("change", atualizarCampos);
});

atualizarCampos();

// Função de sucesso ao escanear o QR Code
function onScanSuccess(decodedText, decodedResult) {
  // Mostra o resultado escaneado
  document.getElementById("result").innerText = `QR Code detectado: ${decodedText}`;
  console.log(`QR Code detectado: ${decodedText}`);
}

// Função para lidar com erros de leitura
function onScanError(errorMessage) {
  console.warn(`Erro ao escanear o QR Code: ${errorMessage}`);
}

// Inicializa o scanner QR Code
const html5QrCode = new Html5Qrcode("reader");

html5QrCode.start(
  { facingMode: "environment" }, // Usa a câmera traseira
  {
    fps: 10,    // Frames por segundo
    qrbox: { width: 250, height: 250 },  // Caixa para a área de escaneamento
  },
  onScanSuccess,
  onScanError
).catch((err) => {
  console.error("Erro ao iniciar o scanner: ", err);
});

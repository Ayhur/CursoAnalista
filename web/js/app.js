(() => {
  const operations = [
    {id:'op-001', date:'2026-07-13T08:00:00Z', status:'pagada', cents:12000, test:false},
    {id:'op-002', date:'2026-07-14T09:30:00Z', status:'rechazada', cents:8000, test:false},
    {id:'op-003', date:'2026-07-15T10:00:00Z', status:'pagada', cents:5000, test:false},
    {id:'op-004', date:'2026-07-16T14:15:00Z', status:'devuelta', cents:3000, test:false},
    {id:'op-005', date:'2026-07-17T12:20:00Z', status:'pendiente', cents:2500, test:false},
    {id:'op-test', date:'2026-07-18T10:00:00Z', status:'pagada', cents:100, test:true},
    {id:'op-fin', date:'2026-07-20T00:00:00Z', status:'pagada', cents:9900, test:false}
  ];
  const correctStates = ['pagada']; const statusOptions = ['pagada','rechazada','pendiente','devuelta'];
  const key = 'cursoanalista-aula-mvp'; let progress = JSON.parse(localStorage.getItem(key) || '{}');
  const setProgress = (lab) => { progress[lab] = true; localStorage.setItem(key, JSON.stringify(progress)); updateProgress(); };
  const updateProgress = () => { document.getElementById('progress-text').textContent = `${Object.keys(progress).length} de 2 laboratorios superados`; };
  const feedback = document.getElementById('grain-feedback');
  document.getElementById('check-grain').addEventListener('click', () => {
    const value = document.querySelector('input[name="grano"]:checked')?.value;
    if (value === 'linea') { feedback.className='feedback good'; feedback.textContent='Correcto: P-01 aparece dos veces porque contiene dos líneas. Contar filas no cuenta pedidos ni clientes.'; setProgress('grano'); }
    else { feedback.className='feedback bad'; feedback.textContent='No todavía. Observa que el mismo pedido aparece una vez por cada artículo incluido.'; }
  });
  document.getElementById('check-cardinality').addEventListener('click', () => {
    const value = document.getElementById('cardinality').value;
    feedback.className = value === 'muchos-uno' ? 'feedback good' : 'feedback bad';
    feedback.textContent = value === 'muchos-uno' ? 'Correcto: un cliente puede tener varios pedidos; cada pedido tiene un cliente en este contrato.' : 'Revisa C-10: tiene P-01 y P-02. Esa repetición determina la cardinalidad.';
  });
  document.getElementById('operations-rows').innerHTML = operations.map(o => `<tr><td>${o.id}</td><td>${o.date}</td><td>${o.status}</td><td>${(o.cents/100).toFixed(2)}</td><td>${o.test?'sí':'no'}</td></tr>`).join('');
  document.getElementById('status-options').innerHTML = statusOptions.map(s => `<label><input type="checkbox" value="${s}"> ${s}</label>`).join('');
  document.getElementById('calculate-report').addEventListener('click', () => {
    const selected = [...document.querySelectorAll('#status-options input:checked')].map(input => input.value);
    const excludeTests = document.getElementById('exclude-tests').checked;
    const exclusiveEnd = document.getElementById('exclusive-end').checked;
    const end = '2026-07-20T00:00:00Z';
    const rows = operations.filter(o => selected.includes(o.status) && (!excludeTests || !o.test) && (!exclusiveEnd || o.date < end));
    const cents = rows.reduce((sum, o) => sum + o.cents, 0);
    const result = document.getElementById('report-result');
    const statesOk = selected.length === 1 && selected[0] === 'pagada';
    const valid = statesOk && excludeTests && exclusiveEnd && cents === 17000;
    if (valid) { result.className='result good'; result.textContent='Resultado verificable: 170,00 EUR. Excluiste la prueba, los estados no pagados y la operación exactamente en el límite final. Ahora revisa la conciliación: elegibles = pagadas + no pagadas.'; setProgress('operaciones'); return; }
    const hints = []; if (!statesOk) hints.push('«Cobrado» solo incluye pagada; una devolución no es un rechazo ni un cobro vigente.'); if (!excludeTests) hints.push('La operación interna de prueba no pertenece al informe.'); if (!exclusiveEnd) hints.push('El final es exclusivo: op-fin pertenece al periodo siguiente.'); if (!hints.length) hints.push('Revisa el contrato y el cálculo de los céntimos.');
    result.className='result bad'; result.textContent=`Tu resultado: ${(cents/100).toFixed(2)} EUR. ${hints.join(' ')}`;
  });
  document.getElementById('reset-progress').addEventListener('click', () => { progress = {}; localStorage.removeItem(key); updateProgress(); });
  updateProgress();
})();

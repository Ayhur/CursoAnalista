// Crea antes dos parámetros de texto: RutaOperaciones y RutaClientes.
// Sustituye sus valores por las rutas locales de los CSV descargados.
let
    OperacionesCrudas = Csv.Document(
        File.Contents(RutaOperaciones),
        [Delimiter=";", Columns=7, Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    CabecerasOperaciones = Table.PromoteHeaders(OperacionesCrudas, [PromoteAllScalars=true]),
    TiposOperaciones = Table.TransformColumnTypes(
        CabecerasOperaciones,
        {{"id_operacion", type text}, {"fecha_hora", type datetime}, {"resultado", type text},
         {"importe", Currency.Type}, {"canal", type text}, {"cliente_id", type text}, {"es_prueba", Int64.Type}},
        "es-ES"
    ),
    SinPruebas = Table.SelectRows(TiposOperaciones, each [es_prueba] = 0),
    ClientesCrudos = Csv.Document(
        File.Contents(RutaClientes),
        [Delimiter=";", Columns=3, Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    CabecerasClientes = Table.PromoteHeaders(ClientesCrudos, [PromoteAllScalars=true]),
    TiposClientes = Table.TransformColumnTypes(
        CabecerasClientes,
        {{"cliente_id", type text}, {"segmento", type text}, {"responsable", type text}}
    ),
    Combinada = Table.NestedJoin(SinPruebas, {"cliente_id"}, TiposClientes, {"cliente_id"}, "cliente", JoinKind.LeftOuter),
    Expandida = Table.ExpandTableColumn(Combinada, "cliente", {"segmento", "responsable"}, {"segmento", "responsable"}),
    MotivoExclusion = Table.AddColumn(
        Expandida, "motivo_exclusion_total",
        each if [resultado] = "pagada" then null
        else if [resultado] = "rechazada" then "Cobro no autorizado o fallido"
        else if [resultado] = "pendiente" then "Resultado aún no definitivo"
        else if [resultado] = "devuelta" then "Pago revertido posteriormente"
        else "Estado no reconocido: investigar",
        type text
    )
in
    MotivoExclusion

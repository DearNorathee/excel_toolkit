import xlwings as xw
def ws_at_wb(ws, wb=None, outputOption=True):
    # If outputOption = True => output WS
    # If outputOption = False => ws_name as string
    # wb could be workbook or string or missing
    # ws could be worksheet or string or missing
    
    try:
        if wb is None:
            wb = ws.book
        elif isinstance(wb, xw.Range):
            wb = xw.Book(wb.value)
        elif wb == "":
            wb = xw.Book.caller()
        else:
            # wb is string
            wb = xw.Book(wb)
    except:
        pass
    
    try:
        wb_name = wb.name
        if ws is None:
            ws02 = xw.Sheet.caller()
        elif isinstance(ws, xw.Range):
            ws02 = wb.sheets[ws.value]
        elif not isinstance(ws, str):
            ws02 = ws
        elif ws == "":
            ws02 = xw.Sheet.caller()
        else:
            # ws is string
            ws02 = wb.sheets[ws]
    except:
        pass
    
    outputWS = wb.sheets[ws02.name]
    if outputOption:
        return outputWS
    else:
        return outputWS.name


def copy_sheet(
    wb: xw.main.Book,
    from_sheet_name: str,
    to_sheet_names: str | list[str],
    )-> None:
    import xlwings as xw
    
    if from_sheet_name not in [s.name for s in wb.sheets]:
        raise KeyError(
            f"Sheet '{from_sheet_name}' not found.  "
            f"Available sheets: {[s.name for s in wb.sheets]}"
        )
        
    app = xw.apps.active
    app.display_alerts = False # to prevent pop-up of copying lambda during copy

    template_sheet = wb.sheets[from_sheet_name]

    if isinstance(to_sheet_names, str):
        to_sheet_names = [to_sheet_names]

    new_sheets = []
    for name in to_sheet_names:
        if to_sheet_names in [s.name for s in wb.sheets]:
            raise KeyError(f'Please pick new name for the sheet. {name} is already taken.')
        new_sheet = template_sheet.copy(before=template_sheet)
        new_sheet.name = name
        new_sheets.append(new_sheet)

    app.display_alerts = True # turn pop-up back on

def sheet_names(wb) -> list[str]:
    
    return [s.name for s in wb.sheets]
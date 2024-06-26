import React from 'react';
import './BoardPanel.css';

interface PieceToImageMap {
  [key: string]: string;
}

const piece_to_image: PieceToImageMap = {
  'p': 'black-pawn',
  'n': 'black-knight',
  'b': 'black-bishop',
  'r': 'black-rook',
  'q': 'black-queen',
  'k': 'black-king',
  'a': 'black-custom1',
  'c': 'black-custom2',
  'd': 'black-custom3',
  'e': 'black-custom4',
  'f': 'black-custom5',
  'g': 'black-custom6',
  'P': 'white-pawn',
  'N': 'white-knight',
  'B': 'white-bishop',
  'R': 'white-rook',
  'Q': 'white-queen',
  'K': 'white-king',
  'A': 'white-custom1',
  'C': 'white-custom2',
  'D': 'white-custom3',
  'E': 'white-custom4',
  'F': 'white-custom5',
  'G': 'white-custom6'
};

interface BoardPanelProps {
  rows: number;
  columns: number;
  isSquare: boolean;
  onRowsChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  onColumnsChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  onSquareToggle: () => void;
  onClearBoard: () => void;
  onResetBoard: () => void;
  onUploadGameMode: () => void;
  onStartGame: () => void;
  selected: { piece: string; color: string } | null;
}

function BoardPanel({
  rows,
  columns,
  isSquare,
  onRowsChange,
  onColumnsChange,
  onSquareToggle,
  onClearBoard,
  onResetBoard,
  onUploadGameMode,
  onStartGame,
  selected,
}: BoardPanelProps) {
  return (
    <div className="board-panel">
      <div className="board-panel-title">Board Properties</div>
      <div className="slider">
        <label htmlFor="rows-slider">Rows: {rows}</label>
        <input
          id="rows-slider"
          type="range"
          min="3"
          max="16"
          value={rows}
          onChange={onRowsChange}
        />
      </div>
      <div className="slider">
        <label htmlFor="columns-slider">Columns: {columns}</label>
        <input
          id="columns-slider"
          type="range"
          min="3"
          max="16"
          value={columns}
          onChange={onColumnsChange}
        />
      </div>
      <div className="toggle-container">
        <label htmlFor="square-toggle">Lock as Square:</label>
        <input
          id="square-toggle"
          type="checkbox"
          checked={isSquare}
          onChange={onSquareToggle}
        />
      </div>
      <button className="board-button" onClick={onClearBoard}>Clear Board</button>
      <button className="board-button" onClick={onResetBoard}>Reset Board</button>
      <button className="start-button" onClick={onStartGame}>Start Game!</button>
      <div className="selected-piece-box">
        {selected && selected.piece ? (
          <img
            src={`/assets/pieces/${piece_to_image[selected.piece]}.png`}
            alt={`${selected.color} ${selected.piece}`}
            className="selected-piece"
          />
        ) : (
          <div className="empty-box"></div>
        )}
      </div>
      <div className="selected-piece-title">Selected Piece</div>
      <button className="board-button program-piece-btn" onClick={onUploadGameMode}>Upload Game Mode</button>

    </div>
  );
}

export default BoardPanel;
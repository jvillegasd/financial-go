import { Component } from "solid-js";

interface Props {
  size?: number;
  width?: number;
  height?: number;
}

const CharityIcon: Component<Props> = ({ size, width, height }) => {
  const calculatedHeight = size || height || 24;
  const calculatedWidth = size || width || 24;

  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width={calculatedWidth}
      height={calculatedHeight}
      viewBox="2.532 2.6 484.468 413.407"
    >
      <path
        d="m265.8 329.7-97.6-97.3a46.8 46.8 0 0 0-66 0 46.3 46.3 0 0 0 0 65.7l97.7 97.3 66-65.7z"
        fill="#FF6E78"
      />
      <path
        d="M117.8 245.3c6.1-6 16-6 22 0l56.9 56.6c6 6 6 15.8 0 21.9-6.1 6-16 6-22 0l-56.9-56.6c-6-6-6-15.9 0-22z"
        fill="#F15561"
      />
      <path
        d="m201.2 331-77-76.7a46.8 46.8 0 0 0-65.9 0 46.3 46.3 0 0 0 0 65.7l77 76.7 66-65.7z"
        fill="#FF9199"
      />
      <path
        d="M56.4 271.7a31.2 31.2 0 0 1 44 0l11 11c6 6 15.9 6 22 0 6-6 15.9-6 22 0l22 21.9c6 6 6 15.8 0 21.9l-44 43.8c-6.1 6-16 6-22 0l-55-54.8a30.9 30.9 0 0 1 0-43.8z"
        fill="#FF8089"
      />
      <path
        d="M377.1 240.7h88v131.4h-48.3c-25.9 0-51.2 7.7-72.7 22a131.3 131.3 0 0 1-72.6 21.8H151.8c-32.1 0-63.2-11.7-87.2-33L17 338.6a43 43 0 0 1-4.5-59.7 43.4 43.4 0 0 1 61.4-5.3l61.4 54.6h175.9v-21.9l13.1-21.9 52.8-43.8z"
        fill="#FFA6AD"
      />
      <path
        d="M179.2 328.3h88a22 22 0 1 1 0 43.8h-88a22 22 0 1 1 0-43.8z"
        fill="#FF9099"
      />
      <path
        d="M443 295.5c0-42.4-44.2-76.7-98.9-76.7-54.6 0-99 34.3-99 76.7h198z"
        fill="#FFC1C6"
      />
      <path
        d="M212.2 240.7h186.9v109.5H212.2a54.9 54.9 0 1 1 0-109.5z"
        fill="#FFA6AD"
      />
      <path
        d="M464.8 350.2a11 11 0 0 0-21.4 0H421v-43.8a22 22 0 0 0-44 0v5.7a67 67 0 0 1-35.8 58c-3.8 2.1-7.5 4.4-11 6.9-17.5 12-38.8 17-60 17H151.8c-26.6 0-52.3-9.6-72.2-27.2L45.3 335a11 11 0 0 0-15.5.5 11 11 0 0 0 .5 15.5l33.4 31h.1v.1h.1l.1.2.2.2.4.3c23 21.3 53.3 33.1 84.7 33.1h122.2c26.8 0 52.3-9 75-23.4 21-13.3 45.3-20.4 70.3-20.4H465v-21.9h-.3z"
        fill="#FF9099"
      />
      <path
        d="M131.2 132.6a65 65 0 0 0 65.2-65 65 65 0 0 0-65.2-65 65 65 0 0 0-65.2 65 65 65 0 0 0 65.2 65z"
        fill="#FFBB2A"
      />
      <path
        d="M131.2 119.6a52 52 0 1 0 .2-104.1 52 52 0 0 0-.2 104z"
        fill="#FFC343"
      />
      <path
        d="M131.2 15.7H127.5l-.2.1H126.3l-.1.1h-.8l-.2.1h-.7v.1h-.7l-.1.1H123v.1h-.5l-.1.1h-.6v.1h-.5l-.1.1h-.5v.1h-.4v.1h-.4l-.1.1h-.4l-.1.1H119l-.2.1H118.6v.1H118.3l-.1.1H117.8v.1h-.4v.1H117.1l-.1.1H116.7v.1h-.4v.1h-.4v.1h-.2l-.1.1h-.2l-.1.1H115v.1H114.7v.1H114.4v.1h-.2l-.1.1h-.2l-.1.1h-.2l-.1.1h-.2l-.1.1h-.2v.1h-.2l-.1.1h-.2v.1H112.2v.1h-.2v.1H111.7v.1h-.2v.1H111.2v.1h-.2v.1h-.2l-.2.1h-.1v.1h-.2v.1h-.2l-.1.1h-.2v.1h-.2v.1h-.2v.1h-.2v.1h-.2l-.1.1h-.1l-.1.1h-.2v.1h-.2v.1h-.2v.1h-.2v.1h-.2v.1h-.2v.1h-.2v.1h-.2v.1h-.1l-.1.1h-.1l-.1.1h-.1l-.1.1h-.1l-.1.1h-.1v.1h-.2v.1h-.1l-.1.1h-.1l-.1.1h-.1v.1h-.2v.1h-.2v.1h-.1l-.1.1h-.1v.1h-.2v.1h-.2v.1h-.1l-.1.1h-.1v.1h-.1l-.1.1h-.1l-.1.1h-.1v.1h-.1l-.1.1h-.1v.1h-.2v.1h-.1v.1h-.2v.1h-.1l-.1.1h-.1v.1h-.1l-.1.1h-.1v.1h-.1l-.1.1h-.1v.1h-.1v.1h-.2v.1h-.1v.1h-.2v.1h-.1v.1h-.1l-.1.1h-.1v.1h-.1l-.1.1-.1.1h-.1v.1h-.2v.1h-.1v.1h-.1v.1h-.2v.1h-.1v.1h-.1l-.1.1-.1.1h-.1v.1h-.1v.1h-.2v.1H99v.1H99v.1h-.1v.1h-.2v.1h-.1v.1h-.1v.1h-.1l-.1.1-.1.1H98v.1H98v.1h-.1v.1h-.1v.1h-.2v.1h-.1v.1h-.1v.1h-.1v.1h-.1v.1H97v.1h-.2v.1h-.1v.1h-.1v.1h-.1v.1h-.1v.1h-.1l-.1.1-.1.1-.1.1H96v.1h-.1v.1h-.1v.1h-.1v.1h-.1v.1h-.1v.1h-.1v.1h-.1v.1h-.1v.1H95v.1H95v.1h-.1v.1h-.1v.1h-.1v.1h-.1l-.1.1-.1.1-.1.1-.1.1v.1H94v.1H94l-.1.1v.1h-.1v.1h-.1v.1h-.1v.1h-.1l-.1.1v.1h-.1v.1h-.1v.1H93v.1H93v.1h-.1v.1h-.1v.1h-.1v.1l-.1.1-.1.1-.1.1v.1h-.1v.1h-.1v.1H92v.1H92v.1h-.1v.1l-.1.1-.1.1-.1.1v.1h-.1v.1h-.1v.1h-.1v.1h-.1v.2H91v.1H91v.1h-.1v.1h-.1v.1l-.1.1-.1.1v.1h-.1v.1h-.1v.1h-.1v.1l-.1.1v.1H90v.1H90v.1l-.1.1-.1.1v.1h-.1v.1l-.1.1v.1h-.1v.1h-.1v.1l-.1.1v.1h-.1v.1H89v.1l-.1.1v.1h-.1v.1l-.1.1-.1.1v.1h-.1v.1l-.1.1v.1h-.1v.1h-.1v.2h-.1v.1H88v.1l-.1.1v.1l-.1.1-.1.1v.1h-.1v.1l-.1.1v.1h-.1v.2h-.1v.1h-.1v.2h-.1v.1H87v.2H87v.1l-.1.1v.1h-.1v.1l-.1.1v.1l-.1.1v.1h-.1v.1l-.1.1v.1l-.1.1v.1h-.1v.2H86v.1l-.1.2h-.1v.2h-.1v.2h-.1v.1l-.1.1v.1l-.1.1v.1l-.1.1v.1h-.1v.1l-.1.1v.1l-.1.1v.1l-.1.1v.1l-.1.1v.1l-.1.1v.1l-.1.1v.1h-.1v.2h-.1v.2h-.1l-.1.3v.1h-.1v.2H84v.2l-.2.3v.2h-.1v.2l-.3.5A51.5 51.5 0 0 0 79.2 64a13 13 0 0 0 13 14 13 13 0 0 0 13-12.2 26.1 26.1 0 0 1 33.3-23c7 2 14.2-2 16.2-8.9a13 13 0 0 0-8.9-16 52.2 52.2 0 0 0-11.5-2h-1l-.1-.1H131.2z"
        fill="#FFD56A"
      />
      <path
        d="M177.3 113.5h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1l.1-.1h.1v-.1h.1v-.1l.1-.1.1-.1.1-.1v-.1h.1l.1-.1.1-.1.1-.1v-.1h.1v-.1h.1l.1-.2h.1v-.1h.1v-.1l.1-.1.1-.1.1-.1v-.1h.1l.1-.2h.1v-.1h.1v-.1h.1v-.1l.1-.1.1-.1.1-.1v-.1h.1v-.1h.1v-.1l.1-.1.1-.1.1-.1v-.1h.1v-.1h.1v-.1l.2-.2v-.1h.1v-.1h.1v-.1l.1-.1.1-.1.1-.1.1-.2.1-.1.1-.1.1-.1v-.1h.1v-.1l.2-.2.1-.2h.1v-.2h.1v-.1h.1v-.1l.1-.1.2-.2v-.1l.1-.1.1-.1v-.1l.1-.1.1-.1v-.1l.2-.1v-.1l.1-.2h.1v-.1l.1-.1v-.1h.1v-.1l.2-.2.1-.2.1-.1v-.1h.1v-.2h.1v-.1h.1v-.1l.1-.1.1-.1v-.2l.2-.2.1-.1v-.1l.2-.2v-.1l.1-.1.1-.2h.1v-.2h.1l.1-.2v-.1h.1v-.2l.2-.1a24.6 24.6 0 0 0 .2-.4l.1-.2.1-.1v-.2a65 65 0 0 0 1.9-3.2v-.1a66.9 66.9 0 0 0 6.3-19.3l.3-1.2v-1l.1-.1V75l.1-.1V74l.1-.2v-1l.1-.1V71.5l.1-.1V69.1l.1-.1v-5.2l-.1-.1v-1.1l-.1-.5a64.7 64.7 0 0 0-5.3-20.8A13 13 0 0 0 167 52a39.1 39.1 0 0 1-39.7 54.5 13 13 0 1 0-2.6 25.9c4.3.4 8.6.4 12.8 0h.5v-.1h.8v-.1h.8v-.1h.7l.1-.1h.6l.1-.1H141.8v-.1h.6v-.1h.5l.3-.1h.1l.7-.2h.1l1.7-.4a65 65 0 0 0 21.2-9l.4-.2.4-.2.3-.2v-.1h.1l.2-.2h.1l.3-.2v-.1h.1l.3-.2.1-.1.3-.2.3-.2.1-.1.2-.2h.1l.1-.1.2-.2h.1l.1-.1.2-.1v-.1h.1l.3-.2v-.1h.1l.1-.1.1-.1h.1v-.1h.1v-.1h.1v-.1h.1l.1-.1.2-.1v-.1h.1v-.1l.2-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1l.1-.1.1-.1h.1v-.1h.1v-.1l.2-.1v-.1h.1l.1-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1l.1-.1.1-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.2v-.2h.1v-.1h.1l.1-.1.1-.1.1-.1.1-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1v-.1h.1z"
        fill="#FF9A00"
      />
      <path
        d="M281.2 184.5c39.6 0 71.7-32 71.7-71.4a71.6 71.6 0 0 0-71.7-71.5 71.6 71.6 0 1 0 0 142.9z"
        fill="#FFC32B"
      />
      <path
        d="M281.2 171.5a58.6 58.6 0 1 0 .2-117.1 58.6 58.6 0 0 0-.2 117.1z"
        fill="#FFC83D"
      />
      <path
        d="M227.4 112.6a13 13 0 0 1-3.6-12A58.6 58.6 0 0 1 268.7 56a13 13 0 1 1 5.6 25.4 32.5 32.5 0 0 0-25 24.8 13 13 0 0 1-22 6.4z"
        fill="#FFD56A"
      />
      <path
        d="M334 74.6a13 13 0 0 0-11.8 18.6 45.6 45.6 0 0 1-41 65.3h-.7c-7.2 0-13 5.8-13.2 13a13 13 0 0 0 12.6 13H281.1c39.7 0 71.8-32 71.8-71.4V109.9h-.1V108.1l-.1-.1V107l-.1-.1V106l-.1-.3v-.6l-.1-.3v-.6c-1-7.8-3.3-15.3-6.7-22.3a13 13 0 0 0-11.8-7.3z"
        fill="#FF9A00"
      />
      <path
        d="M209.5 288.4a91.1 91.1 0 0 0 91.2-90.9c0-50.2-40.8-91-91.2-91a91.1 91.1 0 0 0-91.3 91c0 50.2 40.8 91 91.3 91z"
        fill="#FFD300"
      />
      <path
        d="M209.4 288.4a91.1 91.1 0 0 0 91.3-90.9V193l-.1-.1v-1.6h-.1v-1.4h-.1V188.9l-.1-.1V187.8l-.1-.1V187l-.1-.1v-.7l-.1-.1v-.7h-.1v-.7h-.1v-.5l-.1-.3v-.5l-.1-.3v-.4h-.1v-.6h-.1v-.4l-.1-.2v-.4l-.1-.2v-.4h-.1v-.4l-.1-.3V179.4h-.1v-.5l-.1-.1V178.5l-.1-.4v-.1l-.1-.1V177.6l-.1-.2V177.1l-.1-.1v-.1l-.1-.4v-.2l-.1-.1v-.1l-.1-.5v-.2h-.1l-.1-.6v-.2l-.1-.1-.1-.5v-.2h-.1l-.1-.6v-.1h-.1v-.2l-.2-.5v-.1l-.2-.7v-.2l-.2-.5v-.2h-.1v-.1l-.2-.6-.2-.7v-.2h-.1l-.2-.5V168.4l-.3-.5v-.2l-.2-.6v-.1a169.2 169.2 0 0 0-1.1-3l-.1-.1-.3-.7-.3-.8-.6-1.4-.1-.1-.2-.6-.1-.1-.3-.6v-.2l-.3-.5v-.2h-.1l-.3-.6v-.1l-.3-.5v-.1l-.1-.1-.3-.6-.4-.8-.3-.6v-.1l-.4-.6v-.1l-.4-.7-.4-.6v-.2h-.1l-.2-.5-.1-.1a57.2 57.2 0 0 0-.3-.6l-.1-.1-.4-.6v-.1l-.3-.5v-.1h-.1v-.1h-.1l-.3-.6v-.1h-.1l-.3-.5v-.1h-.1v-.1l-.3-.5h-.1v-.2l-.4-.5v-.1h-.1l-.3-.5v-.1h-.1l-.4-.6v-.1l-.5-.6v-.1a91 91 0 0 0-.4-.5v-.1l-.4-.5-.1-.1v-.1h-.1l-.3-.5-.1-.1-.4-.6-.1-.1v-.1l-.3-.3-.1-.1v-.1h-.1l-.4-.5v-.1h-.1l-.4-.6-.1-.1-.4-.5-.5-.6v-.1c-3.4-4-7-7.8-11-11.1a13 13 0 0 0-18.3 1.3 13 13 0 0 0 1.3 18.3 64.8 64.8 0 0 1-42.7 114 65.1 65.1 0 0 1-35.1-10.2 13 13 0 0 0-18 4 13 13 0 0 0 3.9 17.9c2.3 1.5 4.8 2.9 7.2 4.2h.2l.2.2h.3l.1.2h.2l.2.2h.3l.1.2h.2l.1.1h.2l.1.1.1.1h.2v.1h.2v.1h.2v.1h.2v.1h.2v.1h.2l.1.1h.1l.1.1h.2v.1h.2v.1h.2v.1H172.2v.1h.1l.1.1h.2v.1h.2v.1h.2v.1h.2l.1.1h.2l.1.1h.1l.1.1h.1l.2.1.2.1h.2v.1h.2l.1.1h.1l.1.1h.2l.2.1.2.1.1.1h.1l.2.1h.2l.1.1h.2v.1h.2l.2.1.2.1h.1l.1.1h.2l.2.2H178l.2.1.2.1h.2v.1h.2l.2.1.2.1h.2l.1.1h.2l.2.1.2.1h.3l.2.2H180.8l.3.2h.2l.2.1H181.8l.2.2h.4l.5.2h.2l.1.1h.1l.2.1h.2l.2.1h.2l.5.2h.2l.1.1h.2l.2.1h.2l.2.1.3.1h.2a11.4 11.4 0 0 0 .7.2h.2l.2.1.4.1.2.1H188.2l.2.1h.2l.2.1h.3l.2.1h.2l.2.1H190l.2.1h.2l.3.1h.2l.2.1h.3l.2.1h.4l.3.1h.2l.2.1H193l.2.1h.5l.1.1H194.5v.1h.4l.3.1h.4l.2.1h.6v.1H197l.1.1h.6l.1.1h.7l.1.1H199.6v.1H200.5l.1.1H201.4l.1.1H202.8v.1H204.5v.1H206.9l.1.1H209.5z"
        fill="#FFB800"
      />
      <path
        d="M209.4 262.4a65 65 0 0 0 65.2-64.9 65 65 0 0 0-65.2-65 65 65 0 0 0-65.2 65 65 65 0 0 0 65.2 65z"
        fill="#FFE152"
      />
      <path
        d="M144.2 210.9c-7.2 0-13-5.5-13-12.6v-.8A78.2 78.2 0 0 1 258 136.4a13 13 0 0 1 2.1 18.2 13 13 0 0 1-18.3 2.1 52.1 52.1 0 0 0-84.5 40.8c0 7.2-5.8 13.4-13 13.4z"
        fill="#FFEE9D"
      />
      <path
        d="M229 184.5H190a6.5 6.5 0 1 1 0-13h45.6a13 13 0 1 0 0-26H190a32.5 32.5 0 1 0 0 65H229a6.5 6.5 0 1 1 0 13h-45.6a13 13 0 1 0 0 26H229a32.5 32.5 0 1 0 0-65z"
        fill="#FFF7D2"
      />
      <path
        d="M209.5 236.5a13 13 0 0 1 13 13v13a13 13 0 0 1-26 0v-13a13 13 0 0 1 13-13zM209.5 119.6a13 13 0 0 1 13 13v26a13 13 0 0 1-26 0v-26a13 13 0 0 1 13-13z"
        fill="#FFF7D2"
      />
      <path
        d="M212.2 240.7a54.8 54.8 0 0 0-47.5 27.6 21.8 21.8 0 0 1 36.5 16.2v11a33 33 0 0 0 66 0v-11a22 22 0 0 1 22-21.9H399v-21.9H212.2z"
        fill="#FFC1C6"
      />
      <path
        d="M179.2 295.5a33 33 0 0 0 33 32.8h11a22 22 0 0 0 22-21.9v-21.9a22 22 0 0 0-22-21.9h-11a33 33 0 0 0-33 32.9z"
        fill="#F6EDFF"
      />
      <path
        d="M443 218.8c24.4 0 44 19.6 44 43.8v109.5a43.9 43.9 0 0 1-87.9 0V262.6a43.9 43.9 0 0 1 44-43.8z"
        fill="#5F7BCE"
      />
      <path
        d="M410 262.6c6.2 0 11 5 11 11v87.6a11 11 0 0 1-21.9 0v-87.6c0-6 5-11 11-11z"
        fill="#3F60C4"
      />
    </svg>
  );
};

export default CharityIcon;
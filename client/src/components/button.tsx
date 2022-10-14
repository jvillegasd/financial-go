import { Component, createEffect, createSignal, JSX } from "solid-js";

type ButtonAppearance = "primary" | "outlined" | "link";
type ButtonSize = "m";

interface Props {
  children?: JSX.Element;
  onClick?: () => void;
  appearance?: ButtonAppearance;
  size?: ButtonSize;
  className?: string;
  uppercase?: boolean;
}

function getColors(appearance: ButtonAppearance) {
  if (appearance === "outlined") {
    return "bg-transparent border border-primary text-primary hover:bg-primary hover:text-white focus:ring-2 focus:ring-blue-300 focus:outline-none";
  }
  if (appearance === "link") {
    return "bg-transparent text-blue-600 font-medium leading-tight hover:text-blue-700 hover:bg-gray-100 focus:bg-gray-100 focus:outline-none focus:ring-0 active:bg-gray-200";
  }
  return "hover:bg-blue-700 bg-primary focus:ring-2 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none text-white";
}

function getSpacing(size: ButtonSize) {
  return "p-4 rounded-lg px-12 py-2.5 transition duration-150 ease-in-out";
}

export const Button: Component<Props> = ({
  appearance = "primary",
  size = "m",
  className = "",
  children,
  onClick = () => {},
  uppercase = false,
}) => {
  const [classes, setClasses] = createSignal("");

  createEffect(() => {
    const background = getColors(appearance);
    const spacing = getSpacing(size);
    const uppercaseClass = uppercase ? "uppercase" : "";
    setClasses(
      `inline-block ${background} ${spacing} text-xs font-medium cursor-pointer ${uppercaseClass} ${className}`
    );
  }, [appearance]);

  return (
    <button class={classes()} onClick={onClick}>
      {children}
    </button>
  );
};

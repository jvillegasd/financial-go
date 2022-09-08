import React, { useEffect, useState } from "react";

type ButtonAppearance = "primary" | "outlined" | "link";
type ButtonSize = "m";

interface Props {
  children: React.ReactNode;
  onClick: () => void;
  appearance?: ButtonAppearance;
  size?: ButtonSize;
  className?: string;
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
  return "p-4 rounded-lg px-6 py-2.5 text-xs transition duration-150 ease-in-out";
}

export const Button = ({
  appearance = "primary",
  size = "m",
  className = "",
  children,
  onClick = () => {},
}: Props) => {
  const [classes, setClasses] = useState("");

  useEffect(() => {
    const background = getColors(appearance);
    const spacing = getSpacing(size);
    setClasses(
      `inline-block ${background} ${spacing} cursor-pointer uppercase ${className}`
    );
  }, [appearance]);

  return (
    <button className={classes} onClick={onClick}>
      {children}
    </button>
  );
};

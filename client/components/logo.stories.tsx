import Logo from "./logo";

import type { Meta, StoryObj } from "@storybook/react";

const meta: Meta<typeof Logo> = { component: Logo, title: "Logo" };

type Story = StoryObj<typeof Logo>;

export const Default: Story = {
  args: {},
};

export default meta;
